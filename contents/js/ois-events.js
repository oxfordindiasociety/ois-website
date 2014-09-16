function hideAll() {
  $(".category").removeClass("category-active");
  $(".social").hide();
  $(".fundraising").hide();
  $(".cultural").hide();
  $(".seminar").hide();
}

$(document).ready(function() {
    $("#all-show").click(function() {
      $(".category").removeClass("category-active");
      $(".social").show();
      $(".fundraising").show();
      $(".cultural").show();
      $(".seminar").show();
    });

    $("#fundraising-show").click(function() {
      hideAll();
      $(".fundraising").show();
      $("#fundraising-show").addClass("category-active");
    });
    $("#seminar-show").click(function() {
      hideAll();
      $(".seminar").show();
      $("#seminar-show").addClass("category-active");

    });
    $("#cultural-show").click(function() {
      hideAll();
      $(".cultural").show();
      $("#cultural-show").addClass("category-active");

    });

    $("#social-show").click(function() {
      hideAll();
      $(".social").show();
      $("#social-show").addClass("category-active");

    });

});
