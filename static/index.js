function _one(q, e=document){return e.querySelector(q)}
function _all(q, e=document){return e.querySelectorAll(q)}


const tweetPostElement = document.querySelector('#tweet-post');
const addTweetForm = document.querySelector('.creatTweet');
const btnSubmit = document.querySelector('#submit-main-tweet');
const textEreaInput = document.querySelector('#text-area-input');
const tweetTextElement = document.querySelectorAll('.tweetText');
const updateSubmitBtn = document.querySelector('#update-submit-btn');


function goToUserTweets(user_id) {
  const url = window.location.pathname;
  const user_param_id = url.substring(url.lastIndexOf('/') + 1);
  console.log(user_param_id);

  if(user_id === user_param_id) {
    window.location.href = `/user-account/${user_param_id}`
  } else {
    window.location.href = `/user-profile/${user_id}`
  }
}


/////////////////////////////// TWEET OVERLAY //////////////////////////////////////
function toggleCreateTweetModal(){
    document.querySelector("#createTweetModal").classList.toggle("hidden")
}
function toggleUpdateTweetModal(){
    document.querySelector("#updateTweetModal").classList.toggle("hidden")
}


// let output = '';
// const renderTweets = (tweet) => {
//   output += `
//         <div id="${tweet.tweet_id}" class="p-4 border-t border-slate-200">
//           <div class="flex">
//             <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/user_profile_pictures/${tweet.user_profile_picture}">
//             <div class="w-full pl-4">
//               <!-- first name - username/ text -->
//                 <div id="user-info" class="flex">
//                 <p class="font-bold pr-2">
//                       <span onclick="goToUserTweets('${tweet.user_id}');" class="cursor-pointer">
//                       ${tweet.user_first_name} ${tweet.user_last_name}
//                       </span>
//                     </p>
//                   <p class="font-thin">
//                     @${tweet.user_name}
//                   </p>                        
//                 </div>
//               <div id="tweet-text" class="tweetText pt-2">
//                 ${tweet.tweet_text}
//               </div>
              
//               <div id="tweet-image">
//                 <img class="mt-2 w-full object-cover h-80 tweetImg" src="/images/user_content_images/${tweet.tweet_image}">
//               </div>
//               <div class="flex gap-12 w-10 mt-4 text-lg">
//                   <i class="fa-solid fa-message ml-auto"></i>
//                   <i class="fa-solid fa-heart"></i>
//                   <i class="fa-solid fa-retweet"></i>
//                   <i class="fa-solid fa-share-nodes"></i>
//               </div>
//             </div>
//           </div>
//         </div>
//     `;
//   tweetPostElement.innerHTML = output;
//   hideBrokenImage();
// }


// //-GET-//  -->  /////////// GET TWEETS - FETCH //////////////
// fetch('/tweets')
//     .then(res => res.json())
//     .then(data => {
        
//       for (let tweet of data.tweets) {
//         renderTweets(tweet)
//       }
//     }).catch(error => { 
//       console.log("Server error:", error);
// })





//-POST-//  -->  /////////// CREATE TWEET - FETCH //////////////
async function createTweet(){
    const form = event.target
    // Get the button, set the data-await, and disable it
    const button = _one("button[type='submit']", form)
    button.innerText = button.dataset.await
    // button.innerText = button.getAttribute("data-await")
    button.disabled = true
  
    const url = window.location.pathname;
    const user_id = url.substring(url.lastIndexOf('/') + 1);
  
    const connection = await fetch(`/tweets/${user_id}`, {
      method : "POST",
      body : new FormData(form)
    })
  
    button.disabled = false
    button.innerText = button.dataset.default
  
    if( ! connection.ok ){
      return
    }
    const res = await connection.json();
    const tweet = res.tweet
    
  
    let tweet_post = `
        <div id="${tweet.tweet_id}" class="p-4 border-t border-slate-200">
          <div class="flex">
            <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/user_profile_pictures/${tweet.user_profile_picture}">
            <div class="w-full pl-4">
              <!-- first name - username/ text -->
                <div id="user-info" class="flex">
                    <p class="font-bold pr-2">
                    <span onclick="goToUserTweets('${tweet.user_id}')" class="cursor-pointer">
                      ${tweet.user_first_name} ${tweet.user_last_name}
                    </span>
                    </p>
                  <p class="font-thin">
                    ${tweet.user_name}
                  </p>                        
                </div>
              <div id="tweet-text" class="pt-2">
                ${tweet.tweet_text}
              </div>
              
              <div id="tweet-image">
                <img class="mt-2 w-full object-cover h-80 tweetImg" src="/images/user_content_images/${tweet.tweet_image}">
              </div>
              <div class="flex gap-12 w-10 mt-4 text-lg">
                  <i onclick="edit('${tweet.tweet_id}')" id="edit-post" class="editBtn fa-solid fa-pen cursor-pointer" data-id=${tweet.tweet_id}></i>
                  <i onclick="deleteTweet('${tweet.tweet_id}')" class="fas fa-trash ml-auto cursor-pointer"></i>
                  <i class="fa-solid fa-message ml-auto"></i>
                  <i class="fa-solid fa-heart"></i>
                  <i class="fa-solid fa-retweet"></i>
                  <i class="fa-solid fa-share-nodes"></i>
              </div>
            </div>
          </div>
        </div>
      `
    document.querySelector(".tweet-post").insertAdjacentHTML("afterbegin", tweet_post)
    
  
    _one(".createTweet", form).value = ""
    document.querySelector("#createTweetModal").classList.add("hidden")
  
    hideBrokenImage();
}


//-PUT-//  -->  /////////// UPDATE TWEET - AJAX //////////////
function edit(tweet_id) {
    const tweetID = document.querySelector(`[id='${tweet_id}']`)
    const id = tweetID.id
    const tweetText = document.querySelector(`[id='${tweet_id}']`).children[0].children[1].childNodes[5]
    toggleUpdateTweetModal()
    textEreaInput.value = tweetText.innerText

    if (updateSubmitBtn) {
        updateSubmitBtn.addEventListener('click', (e) => {
          
          $.ajax({
            type: 'PUT',
            url:    `/tweets/${id}`,
            contentType: 'application/json',
            data:   {tweet_text: textEreaInput.value},
            complete: function(response) {
                console.log(response);
            }
          });
          tweetText.innerText = textEreaInput.value
          document.querySelector("#updateTweetModal").classList.add("hidden")     
        })
    } 

}

//-DELETE-//  -->  /////////// DELETE TWEET //////////////
async function deleteTweet(tweet_id) {
    const connection = await fetch(`/tweets/${tweet_id}`, {
        method : "DELETE"
    })
    if (!connection.ok) {
        alert("uppps... try again")
        return
    }

    document.querySelector(`[id='${tweet_id}']`).remove()
}





////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// JQuery - hide borken image //
function hideBrokenImage() {
    $('.userProfile').on("error", function() {
        $(this).attr('src', '/images/user_profile_pictures/default_profile_picture.png');
    });

    // Hide broken img when img not passed
    $(".tweetImg").on("error", function() {
        $(this).hide();
    });
}
