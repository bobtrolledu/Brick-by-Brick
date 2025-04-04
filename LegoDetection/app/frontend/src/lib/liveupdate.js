
var socket = io();
// Listen for updates from the backend
socket.on("update_info", function (data) {
  document.getElementById("brick-id").innerText = data.id;
  document.getElementById("brick-name").innerText = data.name;
  document.getElementById("confidence").innerText = data.confidence;
  document.getElementById("color").innerText = data.color;
});