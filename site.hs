-- site.hs for www.oxfordindiasociety.org.uk
--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE DeriveDataTypeable #-}
import           Control.Applicative        (Alternative (..), (<$>), (<*>))
import           Data.Monoid (mappend, (<>), mconcat)
import           Hakyll
import Data.Binary (Binary (..))
import Data.Typeable (Typeable)
import Data.Maybe (isNothing, fromJust)
import Data.List (isSuffixOf, isInfixOf)
import System.Directory (copyFile)
import Data.String.Utils (replace)
import System.FilePath.Posix (splitExtension)
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
config :: Configuration
config = defaultConfiguration
        {   deployCommand = "rsync -avz ./_site/ arboreal.trenozoic.net:/srv/www/ois-beta/"}

-------------------------------------------------------------------------------------------
removeHtml :: Item String -> Compiler (Item String)
removeHtml item = return $ fmap (withUrls removeStr) item
  where
    removeStr :: String -> String
    removeStr url = case splitExtension url of
        (d, ".html") | isLocal d -> d
        _                        -> url
        where isLocal uri = not (isInfixOf "://" uri)
--------------------------------------------------------------------------------
main :: IO ()
main = hakyllWith config $ do

    match (fromList ["about.mdwn", "contact.mdwn", "prasna-2012.mdwn"]) $ do
        route $ setExtension ".html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    match "fundraising-for-act-for-change/*" $ do
        route idRoute
        compile copyFileCompiler

    match "assets/**" $ do
        route idRoute
        compile copyFileCompiler

    match "js/*" $ do
        route idRoute
        compile copyFileCompiler

    match "fonts/*" $ do
        route idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    --match (fromList ["about.rst", "contact.markdown"]) $ do
    --    route   $ setExtension "html"
    --    compile $ pandocCompiler
    --        >>= loadAndApplyTemplate "templates/default.html" defaultContext
    --        >>= relativizeUrls

    match "photos/**" $ compile compilePhotograph

    match "posts/*" $ do
    --  route $ gsubRoute "posts/" (const "") `composeRoutes` setExtension "html"
        compile postCompiler

    match "about.html" $ do
        route idRoute
        compile $ do
            getResourceBody
            >>= applyAsTemplate defaultContext
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls
            >>= removeHtml
    
    match "events.html" $ do
        route idRoute
        compile $ do
            posts <- recentFirst =<< loadAll "posts/*"
            let indexCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    defaultContext

            getResourceBody
                >>= applyAsTemplate indexCtx
                >>= loadAndApplyTemplate "templates/default.html" indexCtx
                >>= relativizeUrls
                >>= removeHtml

    match "index.html" $ do
        route idRoute
        compile copyFileCompiler

    match "templates/*" $ compile templateCompiler

alternateUrlField :: String -> Context String
alternateUrlField key = field key $
    fmap (maybe empty (replace "photos" key . toUrl)) . getRoute . itemIdentifier

--------------------------------------------------------------------------------------------
postCompiler :: Compiler (Item String)
postCompiler = do
    identifier <- getUnderlying
    imageFolderM <- getMetadataField identifier "images"
    if isNothing imageFolderM then
        pandocCompiler
        >>= loadAndApplyTemplate "templates/post.html"    postCtx
        >>= loadAndApplyTemplate "templates/default.html" postCtx
        >>= relativizeUrls
        >>= removeHtml
    else do
        photos <- loadAll . fromGlob $ "photos/" ++ fromJust imageFolderM ++ "/*"
        let postImgCtx = listField "photos" photographCtx (return photos) <> postCtx
        getResourceBody
            >>= applyAsTemplate postImgCtx
            >>= return . renderPandoc
            >>= loadAndApplyTemplate "templates/post.html"    postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls
            >>= removeHtml

        --getResourceBody
        --    >>= applyAsTemplate postImgCtx
        --    >>= loadAndApplyTemplate "templates/default.html" postImgCtx
        --    >>= return . renderPandoc
        --    >>= relativizeUrls

--------------------------------------------------------------------------------------------
data Photograph = Photograph
    { photoPath :: FilePath
    , photoThumbnail :: FilePath
    , photoIcon :: FilePath
    } deriving (Show, Typeable)

--------------------------------------------------------------------------------------------
instance Binary Photograph where
    get = Photograph <$> get <*> get <*> get

    put (Photograph photoPath photoThumbnail photoIcon) =
        put photoPath >> put photoThumbnail >> put photoIcon

instance Writable Photograph where
    write fp item = copyFile (photoPath (itemBody item)) fp

compilePhotograph :: Compiler (Item Photograph)
compilePhotograph = do
    filePath <- toFilePath <$> getUnderlying
    let iconPath = replace "photos" "icons" filePath
        thumbnailPath = replace "photos" "thumbnails" filePath

    makeItem Photograph
        { photoPath = prefix filePath
        , photoThumbnail = prefix thumbnailPath
        , photoIcon = prefix iconPath
        }
    where prefix = (++) "http://data.oxfordindiasociety.org.uk/"

photographCtx :: Context Photograph
photographCtx = mconcat
    [ field "original" $ return . show . photoPath . itemBody
    , field "thumbnail" $ return . show . photoThumbnail . itemBody
    , field "icon" $ return . show . photoIcon . itemBody
    , urlField "url"
    ]

--------------------------------------------------------------------------------
--galleryField :: String -> Context String
--galleryField key = field key $ \i -> do
--    imageFolder <- getMetadataField' (itemIdentifier i) "images"
--    fileList <- unsafeCompiler $ getDirectoryContents (basePath ++ "photos/" ++ imageFolder)
--    return $ intercalate "," $ filter (extensions [".JPG", ".jpg"]) fileList

--------------------------------------------------------------------------------
-- | Returns true if filename has one of the extensions
extensions :: [String] -> String -> Bool
extensions exts filename = or [e `isSuffixOf` filename | e <- exts]

--------------------------------------------------------------------------------
-- | Post context, in this case have event location, time etc.
postCtx :: Context String
postCtx = dateField "date" "%d %b, %Y" <> defaultContext
