function hideAll() {
        $("li").removeClass("active");

  $(".social").hide();
  $(".fundraising").hide();
  $(".cultural").hide();
  $(".seminar").hide();
  $(".sports").hide();
}

$(document).ready(function() {
    $('.carousel').slick({
      autoplay: true,
      arrows: false
    });
    $("#all-show").click(function() {
      $(".social").show();
      $(".fundraising").show();
      $(".cultural").show();
      $(".seminar").show();
      $(".sports").show();
    });

    $("#fundraising-show").click(function() {
      hideAll();
      $(".fundraising").show();
      $(".fundraising").parent().addClass("active");
    });
    $("#seminar-show").click(function() {
      hideAll();
      $(".seminar").show();
    });
    $("#cultural-show").click(function() {
      hideAll();
      $(".cultural").show();
    });

    $("#social-show").click(function() {
      hideAll();
      $(".social").show();
    });
    $("#sports-show").click(function() {
      hideAll();
      $(".sports").show();
    });
    $('#fullpage').fullpage();

});
