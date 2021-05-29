console.log("end");
points = sessionStorage.getItem("points");

$("#send-my-url-to-django-button").click(function () {
    console.log(points);
    $.ajax({
        url: "gettingResult",
        type: "POST",
        dataType: "json",
        data: {
        points: points,
        csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function (json) {
        alert("Successfully sent the URL to Django");
        },
        // error: function (xhr, errmsg, err) {
        // console.log("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
        // }
    });


    // $.ajax({
    //     type: 'POST',
    //     url: "gettingResult",
    //     data: points,
    //     success: function (response) {
    //        console.log("success")
    //     },
    //     error: function (response) {
    //         // alert the error if any error occured
    //         alert(response["responseJSON"]["error"]);
    //     }
    // })
    
});
