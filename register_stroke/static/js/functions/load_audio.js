function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// Set up basic variables for app
const record = document.querySelector(".record");
const stop = document.querySelector(".stop");
const soundClips = document.querySelector(".sound-clips");
const canvas = document.querySelector(".visualizer");
const mainSection = document.querySelector(".main-controls");

// Disable stop button while not recording


// Visualiser setup - create web audio api context and canvas


// Main block for doing the audio recording
if (navigator.mediaDevices.getUserMedia) {
  console.log("The mediaDevices.getUserMedia() method is supported.");

  const constraints = { audio: true };
  let chunks = [];

  let onSuccess = function (stream) {
    const mediaRecorder = new MediaRecorder(stream);



    record.onclick = function () {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("Recorder started.");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    };

    stop.onclick = function () {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("Recorder stopped.");
      record.style.background = "";
      record.style.color = "";

      stop.disabled = true;
      record.disabled = false;
    };

    mediaRecorder.onstop = function (e) {
      console.log("Last data to read (after MediaRecorder.stop() called).");

      const clipName = prompt(
        "Enter a name for your sound clip?",
        "My unnamed clip"
      );

      const clipContainer = document.createElement("article");
      const clipLabel = document.createElement("p");
      const audio = document.createElement("audio");
      const deleteButton = document.createElement("button");
      //
      const resultButton = document.createElement("button");
      const newDiv = document.createElement("div");
      const cardBodyDiv = document.createElement('div');
      //
      const uniqueID = `id-${Date.now().toString(36)}-${Math.random().toString(36).slice(2)}`;
      deleteButton.setAttribute('id', uniqueID);
      resultButton.setAttribute('id', uniqueID);
      console.log(deleteButton.id)

      clipContainer.className = 'border rounded'
      clipContainer.classList.add("clip");
      //
  
      audio.setAttribute("controls", "");
      deleteButton.textContent = "Delete";
      deleteButton.className = "delete btn btn-outline-danger m-2";
      resultButton.textContent = "Result";
      resultButton.className = "result btn btn-outline-primary m-2";

      //
      newDiv.className = "card m-2"
      cardBodyDiv.className = "card-body"
      newDiv.appendChild(cardBodyDiv);
      //

      if (clipName === null) {
        clipLabel.textContent = "My unnamed clip";
      } else {
        clipLabel.textContent = clipName;
      }

      clipContainer.appendChild(audio);
      clipContainer.appendChild(clipLabel);
      clipContainer.appendChild(deleteButton);
      //
      clipContainer.appendChild(resultButton);
      clipContainer.appendChild(newDiv);
      //
      soundClips.appendChild(clipContainer);

      audio.controls = true;
      const blob = new Blob(chunks, { type: "audio/wav" });
      chunks = [];
      const audioURL = window.URL.createObjectURL(blob);
      audio.src = audioURL;

      var reader = new FileReader();
      reader.readAsDataURL(blob);
      reader.onloadend = function() {
        var base64Data = reader.result;
        console.log('stop click')
        fetch('analysis/', {method: "POST", credentials: "same-origin", headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
              'Content-Type': 'application/json'},
              body: JSON.stringify({
                data: base64Data,
                'id_data': uniqueID
              })
        })
        .then(response => response.json()) // converts the response to JSON
        .then(data => {
              console.log(data);
              // do something (like update the DOM with the data)
              alert(data['text'])
              cardBodyDiv.textContent = data['text'];
        });
      };




      deleteButton.onclick = function (e) {
        //
        console.log(deleteButton.id);
        e.target.closest(".clip").remove();
        //
        fetch('delete/', {method: "POST", credentials: "same-origin", headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
              'Content-Type': 'application/json'},
              body: JSON.stringify({
                'id_data': deleteButton.id
              })
        })
        .then(response => response.json()) 
        .then(data => {
              console.log(data);
              alert(data['messege']);

        });
        //
      };

      clipLabel.onclick = function () {
        const existingName = clipLabel.textContent;
        const newClipName = prompt("Enter a new name for your sound clip?");
        if (newClipName === null) {
          clipLabel.textContent = existingName;
        } else {
          clipLabel.textContent = newClipName;
        }
      };
    };

    mediaRecorder.ondataavailable = function (e) {
      chunks.push(e.data);
    };
  };

  let onError = function (err) {
    console.log("The following error occured: " + err);
    alert('Проблемы подключния микрофона. Вы не сможете воспользоваться функцией записи голоса. Подключите микрофон, обновите страницу. Включите кнопку Record, при записи изменится цвет кнопики на красный.');
  };

  navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);

  
  
} else {
  console.log("MediaDevices.getUserMedia() not supported on your browser!");
}
