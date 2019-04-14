
console.log("It worked!");

    //Pop-up stuff
    document.body.innerHTML += '<dialog id="dialog" style="width: 320px; height: 320px;"><center><font size = "+10">Smile!</font></center><center><br><button>Close</button></center><video id="video" width="320" height="240" autoplay="true"></video></dialog>';
    var dialog = document.querySelector("dialog")
    dialog.querySelector("button").addEventListener("click", function() {
        dialog.close()
    })
    dialog.showModal();

    const script = document.createElement('script');

    document.getElementById('dialog').appendChild(script);

    //Stuff to access camera
    var video = document.querySelector("#video");
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {video.srcObject = stream})

        .catch(function (err0r) {
            console.log(err0r);
        });
    }

    const canvas = document.createElement('canvas');
    canvas.id = "screenshot";
    document.getElementById("dialog").appendChild(canvas);
    video.onclick= async function() {
        console.log("Omg we got clicked on!")
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        console.log(canvas);
        // Other browsers will fall back to image/png
        var image = canvas.toDataURL('image/webp');
        var r = new FileReader();
        r.onload = function(){alert(r.result);};
        console.log(image);

        src = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js';
        processImage();



        function processImage() {
            // Replace <Subscription Key> with your valid subscription key.
            var subscriptionKey = "24c30a3980384e43bd3cd274a360dcc8";

            // NOTE: You must use the same region in your REST call as you used to
            // obtain your subscription keys. For example, if you obtained your
            // subscription keys from westus, replace "westcentralus" in the URL
            // below with "westus".
            //
            // Free trial subscription keys are generated in the "westus" region.
            // If you use a free trial subscription key, you shouldn't need to change
            // this region.
            var uriBase =
                "https://westus.api.cognitive.microsoft.com/face/v1.0/detect";

            // Request parameters.
            var params = {
                "returnFaceAttributes": "smile"
            };

            var imageURL = ("https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg").value;

            console.log("Requested!");

            // Display the image.
            // var sourceImageUrl = document.getElementById("inputImage").value;
            // document.querySelector("#sourceImage").src = sourceImageUrl;

            // Perform the REST API call.
            $.ajax({
                url: uriBase + "?" + $.param(params),

                // Request headers.
                beforeSend: function(xhrObj){
                    xhrObj.setRequestHeader("Content-Type","application/json");
                    xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", subscriptionKey);
                },

                type: "POST",

                // Request body.
                data: '{"url": ' + '"' + imageURL + '"}',
            })


            .done(function(data) {
                // Show formatted JSON on webpage.
                console.log("Done!");
                console.log("Smile: " + data.smile);
                $("#responseTextArea").val(JSON.stringify(data, null, 2));
                if(data.smile > .75){
                    dialog.close()
                }
            })





            .fail(function(jqXHR, textStatus, errorThrown) {
                // Display error message.
                var errorString = (errorThrown === "") ?
                    "Error.jjjjj " : errorThrown + " (" + jqXHR.status + "): ";
                errorString += (jqXHR.responseText === "") ?
                    "" : (jQuery.parseJSON(jqXHR.responseText).message) ?
                        jQuery.parseJSON(jqXHR.responseText).message :
                            jQuery.parseJSON(jqXHR.responseText).error.message;
                alert(errorString);
            });
        };
        //const detections = await detectAllFaces(image);
        //console.log(detections)


        // function binEncode(data) {
        //     var binArray = []
        //     var datEncode = "";
        //
        //     for (i=0; i < data.length; i++) {
        //         binArray.push(data[i].charCodeAt(0).toString(2));
        //     }
        //     for (j=0; j < binArray.length; j++) {
        //         var pad = padding_left(binArray[j], '0', 8);
        //         datEncode += pad + ' ';
        //     }
        //     function padding_left(s, c, n) { if (! s || ! c || s.length >= n) {
        //         return s;
        //     }
        //     var max = (n - s.length)/c.length;
        //     for (var i = 0; i < max; i++) {
        //         s = c + s; } return s;
        //     }
        //     console.log(binArray);
        // }
    };
