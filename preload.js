// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.
const os = require('os');
const fs = require('fs');
const child_process = require('child_process');
const iconv = require('iconv-lite');

window.addEventListener('DOMContentLoaded', () => {
  var timeoutID = null;

  $(document).ready(function () {
    $("#startBtn").click(function () {
      if (timeoutID == null)
        timeoutID = window.setInterval(() =>
          getTraffic().then(function (data) {
            TrafficInfo = data.split("\n");
            result = '';
            for (i = 0; i < TrafficInfo.length - 1; i = i + 3) {
              result += `<tr><td>${TrafficInfo[i]}</td><td>${TrafficInfo[i + 1]}</td><td>${TrafficInfo[i + 2]}</td></tr>`;
            }
            $("#tableBody").html(result);
          }), 1000);
    });
  });

  $(document).ready(function () {
    $("#stopBtn").click(function () {
      if (timeoutID != null) {
        clearInterval(timeoutID);
        timeoutID = null;
      }
    });
  });
})

function getTraffic() {
  return new Promise((resolve, reject) => {
    var workerProcess = child_process.spawn('python', ['networkTraffic.py', { encoding: 'buffer' }, 0]);
    var result = '';

    workerProcess.stdout.on('data', function (data) {
      result += iconv.decode(data, 'big5').toString();
    })

    workerProcess.stderr.on('data', function (data) {
      reject(data);
    });

    workerProcess.on('close', function (code) {
      resolve(result);
    });
  })
}
