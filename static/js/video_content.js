setTimeout(()=>{
  if (localStorage.getItem("watched_videos") == null){
      console.log("{{Video_info['id']}}")
      VideoArray = []
      VideoArray.push("{{Video_info['id']}}")
      localStorage.setItem("watched_videos", JSON.stringify(VideoArray))
    }
    else{
    console.log("{{Video_info['id']}}")
    item = localStorage.getItem("watched_videos")
    VideoArray = JSON.parse(item)
    new_video = true
    VideoArray.forEach(ele => {
      if(ele == "{{Video_info['id']}}"){
        new_video = false
      }
    })
    if(new_video){
      VideoArray.push("{{Video_info['id']}}"),
      localStorage.setItem("watched_videos", JSON.stringify(VideoArray));
    }
  }
}, 5000)
width = window.innerWidth > 0 ? window.innerWidth : screen.width;
go_back = document.getElementById("go_back");
go_next = document.getElementById("go_next");

if (width < 1050) {
  go_back.classList.add("hide");
  go_next.classList.add("hide");
}
hljs.highlightAll(), (globle_id = "full-code1");
var input_name = document.getElementById("name"),
  input_comment = document.getElementById("comment"),
  name_value = null,
  comment_value = null;

function copy_code(t) {
  var e = document.querySelector("#" + globle_id).innerText;
  navigator.clipboard.writeText(e).then(
    function () {},
    function () {
      console.error("Can't Copy code");
    }
  ),
    (copy_btn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-check-all" viewBox="0 0 16 16">       <path d="M8.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L2.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093L8.95 4.992a.252.252 0 0 1 .02-.022zm-.92 5.14.92.92a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 1 0-1.091-1.028L9.477 9.417l-.485-.486-.943 1.179z"/>     </svg><b> Copied</b>'),
    setTimeout(() => {
      copy_btn.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-clipboard mb-1" viewBox="0 0 16 16">             <path  d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>              <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>           </svg><b> Copy </b>';
    }, 3e3);
}

  console.log("File imported"),
  (copy_btn = document.getElementById("copy-btn")),
  (copy_btn.innerHTML =
    '<svg  xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-clipboard mb-1" viewBox="0 0 16 16">           <path  d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"/>    <path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"/>         </svg><b> Copy</b>'),
  copy_btn.addEventListener("click", copy_code),
  (hide = !0),
  (hide_btn = document.getElementById("hide-btn")),
  (video = document.getElementById("video")),
  hide_btn.addEventListener("click", () => {
    hide
      ? ((hide = !1),
        video.classList.add("hide"),
        (hide_btn.innerHTML =
          'Show Video <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="mb-1 bi bi-eye-fill" viewBox="0 0 16 16">     <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>     <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/>     </svg>'))
      : ((hide = !0),
        video.classList.remove("hide"),
        (hide_btn.innerHTML =
          'Hide Video <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="mb-1 bi bi-eye-slash-fill" viewBox="0 0 16 16">     <path d="m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7.029 7.029 0 0 0 2.79-.588zM5.21 3.088A7.028 7.028 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474L5.21 3.089z"/>       <path d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829l-2.83-2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12-.708.708z"/>         </svg>'));
  })
