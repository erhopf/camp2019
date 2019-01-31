---
title: Understanding the Javascript
nav_order: 3
parent: Extra credit
permalink: /sign-up
nav_exclude: true
---

*Note: Not sure if I'm going to keep this section.*

# Introduction

This application relies on Javascript and jQuery to hit our Flask app and handle the responses. In this section, we're going to look more closely at the code in `main.js`, specifically the Ajax and XHR requests.

## Calling the translate-text route

```javascript
//Translate text with flask route
$("#translate").on("click", function(e) {
  e.preventDefault();
  var translateVal = document.getElementById("text-to-translate").value;
  var languageVal = document.getElementById("select-language").value;
  var translateRequest = { 'text': translateVal, 'to': languageVal }

  if (translateVal !== "") {
    $.ajax({
      url: '/translate-text',
      method: 'POST',
      headers: {
          'Content-Type':'application/json'
      },
      dataType: 'json',
      data: JSON.stringify(translateRequest),
      success: function(data) {
        for (var i = 0; i < data.length; i++) {
          document.getElementById("translation-result").textContent = data[i].translations[0].text;
          document.getElementById("detected-language-result").textContent = data[i].detectedLanguage.language;
          if (document.getElementById("detected-language-result").textContent !== ""){
            document.getElementById("detected-language").style.display = "block";
          }
          document.getElementById("confidence").textContent = data[i].detectedLanguage.score;
        }
      }
    });
  };
});
```

## Calling the analyze-sentiment route

```javascript
//Run sentinment analysis on input and translation.
$("#sentiment-analysis").on("click", function(e) {
  e.preventDefault();
  var inputText = document.getElementById("text-to-translate").value;
  var inputLanguage = document.getElementById("detected-language-result").innerHTML;
  var outputText = document.getElementById("translation-result").value;
  var outputLanguage = document.getElementById("select-language").value;

  var sentimentRequest = { "inputText": inputText, "inputLanguage": inputLanguage, "outputText": outputText, "outputLanguage": outputLanguage };

  if (inputText !== "") {
    $.ajax({
      url: '/sentiment-analysis',
      method: 'POST',
      headers: {
          'Content-Type':'application/json'
      },
      dataType: 'json',
      data: JSON.stringify(sentimentRequest),
      success: function(data) {
        for (var i = 0; i < data.documents.length; i++) {
          if (typeof data.documents[i] !== 'undefined'){
            if (data.documents[i].id === "1") {
              document.getElementById("input-sentiment").textContent = data.documents[i].score;
            }
            if (data.documents[i].id === "2") {
              document.getElementById("translation-sentiment").textContent = data.documents[i].score;
            }
          }
        }
        for (var i = 0; i < data.errors.length; i++) {
          if (typeof data.errors[i] !== 'undefined'){
            if (data.errors[i].id === "1") {
              document.getElementById("input-sentiment").textContent = data.errors[i].message;
            }
            if (data.errors[i].id === "2") {
              document.getElementById("translation-sentiment").textContent = data.errors[i].message;
            }
          }
        }
        if (document.getElementById("input-sentiment").textContent !== '' && document.getElementById("translation-sentiment").textContent !== ''){
          document.getElementById("sentiment").style.display = "block";
        }
      }
    });
  }
});
```

## Calling the text-to-speech route

```javascript
// Convert text-to-speech
$("#text-to-speech").on("click", function(e) {
  e.preventDefault();
  var ttsInput = document.getElementById("translation-result").value;
  var ttsVoice = document.getElementById("select-voice").value;
  var ttsRequest = { 'text': ttsInput, 'voice': ttsVoice }

  var xhr = new XMLHttpRequest();
  xhr.open('post', '/text-to-speech', true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.responseType = "blob";
  xhr.onload = function(evt){
    if (xhr.status === 200) {
      audioBlob = new Blob([xhr.response], {type: "audio/mpeg"});
      audioURL = URL.createObjectURL(audioBlob);
      if (audioURL.length > 5){
        var audio = document.getElementById('audio');
        var source = document.getElementById('audio-source');
        source.src = audioURL;
        audio.load();
        audio.play();
      }else{
        console.log("An error occurred getting and playing the audio.")
      }
    }
  }
  xhr.send(JSON.stringify(ttsRequest));
});
```
