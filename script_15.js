function makeGetRequest(path) {
  return new Promise(function (resolve, reject) {
      $.get(path,{async:false}).then(
          (response) => {
              result = $.parseJSON(response)
              // var result = response.data;
              // console.log('Processing Request');
              resolve(result);
          },
              (error) => {
              reject(error);
          }
      );
  });
}

// async function gt() {
//   var result = await makeGetRequest('http://127.0.0.1:5000/matrix');
//   return result
// }

var data = {}
var res = gt()

// res.then(async function(v) {
//     data = v
//     console.log(data)
//     matx = data['img']
//     size = data['size']
//     console.log(size)
//     console.log(matx)
// });

async function getdata(){
  let type = document.getElementById("changepm").value
  let date = document.getElementById("changedate").value
  let time = document.getElementById("changetime").value
  res = makeGetRequest('http://34.101.175.5/matrix?Date='+date+'&Time='+time+'&type='+type);
}

async function main() {
  await res.then(async function(v) {
    data = v
    matx = data['img']
    size = data['size']
  });

  matx = data['img']
  size = data['size']
  
  // Setup our variables
  var cH = $('#crosshair-h'),
      cV = $('#crosshair-v');

  $(this).on('mousemove touchmove', function(e) {

    rect = document.getElementById('image').getBoundingClientRect()

    var x = e.pageX - 1-rect.left;
    var y = e.pageY - 1-rect.top;
    x = Math.round(x)
    y = Math.round(y)

    if (x > size[0] || x < 0 || y > size[1] || y < 0){
      ans = 0
      document.getElementById('mousepos').style.visibility = "hidden"
    }
    else {
      document.getElementById('mousepos').style.visibility = "visible"
      ans = matx[y][x]

      cH.css('top', e.pageY);
      cV.css('left', e.pageX);
    
      $('#mousepos').css({
        top: e.pageY + 'px',
        left: e.pageX + 'px'
      }, 800);
      $('#mousepos').text( ans);
      e.stopPropagation();
    }
    
  });
  e.stopPropagation();
}

$(document).ready(main());