

$(document).ready(function() {

    $(this).attr("id").click(function (e) {
        e.preventDefault();
        $(".popup, .popup-content").addClass("active");
        // $("#detal_view").
    });

    $(".close, .popup").on("click", function(e){
        e.preventDefault();
        $(".popup, .popup-content").removeClass("active");
        });
});



