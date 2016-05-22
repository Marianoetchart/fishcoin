/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var HTML = "";
var lastselectedelement = null;

var _weight = "";
var _type = "";
var _location = "";
var _photo = "";
var _code = "4TX68O";

var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
        StatusBar.hide();

        //Load fish food data
        $.getJSON("data/seafoodlist.json", function(json) {
            
            for(var j=0; j<json.length; j++){
                HTML = HTML + '<div class="selectedfish">';
                HTML = HTML + '<h4>Market Name : ' + json[j]['MARKET NAME S'] + '</h4><p>Common Name : ' + json[j]['COMMON NAME'] + '</p><p>Scientific Name : ' + json[j]['SCIENTIFIC NAME'] + '</p>';
                HTML = HTML + '</div>';
            }
            
            $("#type").append(HTML);
            
            $(".selectedfish").click(function(element){
                if(lastselectedelement != null){
                    $(lastselectedelement).closest(".selectedfish").css("background", "white");
                    _type 
                }
                lastselectedelement = element.target;
                $(element.target).closest(".selectedfish").css("background-color", "#fcbe32");
            });
        });
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        /*$("#scan-qr").click(function(){
            alert(cordova.plugins);
           cordova.plugins.barcodeScanner.scan(
              function (result) {
                  alert("We got a barcode\n" +
                        "Result: " + result.text + "\n" +
                        "Format: " + result.format + "\n" +
                        "Cancelled: " + result.cancelled);
              }, 
              function (error) {
                  alert("Scanning failed: " + error);
              }
           ); 
        });*/
        
        navigator.globalization.getPreferredLanguage(LanguageSuccess, LanguageError);
        console.log('Received Event: ' + id);
    }
};

function LanguageSuccess(lang){
    console.log(lang.value);
}

function LanguageError(err){
    console.log(err);
}

var pageArray = ["#p1", "#p2", "#p3", "#p4", "#p5"];
var currentPage = 0;
var selectedapp = "";

$(".next_btn").click(function(){
    NextPage();
});

$(".buy_btn").click(function(){
    currentPage++;
    NextPage();
});

$(".sell_btn").click(function(){
    currentPage++;
    NextPage();
});
/*$("#tradefish-app #p2").click(function(){
    currentPage++;
    NextPage();
});
$("#tradefish-app #p3").click(function(){
    NextPage();
});*/

$("nav").click(function(){
    PrevPage();
});

$("#take-picture").click(function(){
   navigator.camera.getPicture(onSuccess, onFail, { 
        quality: 100,
        destinationType: Camera.DestinationType.FILE_URI
    }); 
});

$("#tradefish-btn").click(function(){
    selectedapp = "#tradefish-app";
    
    $("#tradefish-app").css("display", "block");
    $("#tradefish-app #p1").css("display", "block"); 
    $("#selection-screen").css("display", "none");
}); 

$("#registeruser-btn").click(function(){
    
    selectedapp = "#admin-app";
    
    $("#admin-app").css("display", "block");
    $("#admin-app #p1").css("display", "block");
    $("#selection-screen").css("display", "none");
});

$("#scancode-btn").click(function(){
    /*$.ajax({
         type:"POST",
         url:"http://192.168.136.198:8181/api/fish/",
         data: {
            "code": "8t6t88",
            "weight": "300",
            "type": "tuna",
            "species": "null",
            "latitude": null,
            "longitude": null,
            "photo": ""
        },
         success: function(data){
             console.log(data);
         }
    });*/
    
    selectedapp = "#scan-app";
    
    $("#scan-app").css("display", "block");
    $("#scan-app #p1").css("display", "block");
    $("#selection-screen").css("display", "none");
});

var dataURL = "";
$("#generatedata_btn").click(function(){
    _weight = $("#weight").val();
    
    $("#p5 .weight").text("Weight: " + _weight);
    $("#p5 .type").text("Type: " + _type);
    $("#p5 .code").text(_code);
    NextPage();
    
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    var img = document.getElementById("photo-display");
    ctx.drawImage(img, c.width, c.height);
    dataURL = c.toDataURL();
    
   $.ajax({
         type:"POST",
         url:"http://192.168.136.200:8888/fish/call.php",
         data: {
            "code": "8t6t88",
            "weight": "300",
            "type": "tuna",
            "species": "null",
            "latitude": null,
            "longitude": null,
            "photo": dataURL
        },
         success: function(data){
             alert(data);
         }
    });
});
 
function onSuccess(imageData) {
    currentPage++;
    $("#take-picture").closest(".page").css("display", "none");
    $(pageArray[currentPage]).css("display", "block");
    
    var image = document.getElementById("photo-display");
    image.src = imageData;
}
 
function onFail(message) {
    alert('Failed because: ' + message);
}

function NextPage(){
    // Change your html here
    currentPage++;
    $(".page").each(function(){
        $(this).css("display", "none");
    });
    $(selectedapp + " " + pageArray[currentPage]).css("display", "block");
}

function PrevPage(){
    // Change your html here
    if(currentPage <= 0){
        $("#admin-app").css("display", "none");
        $("#scan-app").css("display", "none");
        $("#tradefish-app").css("display", "none");
        $("#selection-screen").css("display", "block");
    }else{
        currentPage--;
        $(".page").each(function(){
            $(this).css("display", "none");
        });
        $(selectedapp + " " + pageArray[currentPage]).css("display", "block");
    }
}

app.initialize();