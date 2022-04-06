function _one(q, e=document){return e.querySelector(q)}
function _all(q, e=document){return e.querySelectorAll(q)}


const tweetPostElement = document.querySelector('#tweet-post');
const addTweetForm = document.querySelector('.creatTweet');
const editButton = document.querySelector('.editBtn');
const textEreaInput = document.querySelector('#text-area-input');
const btnSubmit = document.querySelector('#submit-main-tweet');
const tweetTextElement = document.querySelector('#tweet-text')

let output = '';

/////////////////////////////// TWEET OVERLAY //////////////////////////////////////
function toggleTweetModal(){
    document.querySelector("#tweetModal").classList.toggle("hidden")
}


// /////////////////////////////// Method calls //////////////////////////////////////
hideBrokenImage();





const renderTweets = (post, tweet_id) => {
        output += `
        <div id="${tweet_id}" class="p-4 border-t border-slate-200">
        <div class="flex">
          <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/user_profile_pictures/${post.user_profile_picture}">
          <div class="w-full pl-4">
            <!-- first name - username/ text -->
              <div id="user-info" class="flex">
              <p class="font-bold pr-2">
                    <a href="/user-tweets/${post.user_id}" onclick="spa(); return false">
                    ${post.user_first_name} ${post.user_last_name}
                    </a>
                  </p>
                <p class="font-thin">
                  ${post.user_name}
                </p>                        
              </div>
            <div id="tweet-text" class="pt-2">
              ${post.tweet_text}
            </div>
            
            <div id="tweet-image">
              <img class="mt-2 w-full object-cover h-80 tweetImg" src="/images/user_content_images/${post.tweet_image}">
            </div>
            <div class="flex gap-12 w-10 mt-4 text-lg">
                <i id="delete-post" onclick="edit('${tweet_id}')" class="editBtn fa-solid fa-pen cursor-pointer"></i>
                <i onclick="deleteTweet('${tweet_id}')" class="fas fa-trash ml-auto cursor-pointer"></i>
                <i class="fa-solid fa-message ml-auto"></i>
                <i class="fa-solid fa-heart"></i>
                <i class="fa-solid fa-retweet"></i>
                <i class="fa-solid fa-share-nodes"></i>
            </div>
          </div>
        </div>
      </div>
    `;
    tweetPostElement.innerHTML = output;
    hideBrokenImage();

}

// Get - Tweets
// Method: GET
fetch('/tweets')
    .then(res => res.json())
    .then(data => {
        
        data.tweet_id.forEach(tweet_id => {
            const post = data.tweets[tweet_id]
            renderTweets(post, tweet_id)   
        });
    })

// Create - Tweet
// Method: POST


async function sendTweet(){
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
    const element = res.tweet
    const tweet_id = res.tweet_id
    console.log(tweet_id)
    
  
    let tweet_post = `
        <div id="${tweet_id}" class="p-4 border-t border-slate-200">
          <div class="flex">
            <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/user_profile_pictures/${element.user_profile_picture}">
            <div class="w-full pl-4">
              <!-- first name - username/ text -->
                <div id="user-info" class="flex">
                    <p class="font-bold pr-2">
                    <a href="/user-tweets/${element.user_id}" onclick="spa(); return false">
                      ${element.user_first_name} ${element.user_last_name}
                    </a>
                    </p>
                  <p class="font-thin">
                    ${element.user_name}
                  </p>                        
                </div>
              <div id="tweet-text" class="pt-2">
                ${element.tweet_text}
              </div>
              
              <div id="tweet-image">
                <img class="mt-2 w-full object-cover h-80 tweetImg" src="/images/user_content_images/${element.tweet_image}">
              </div>
              <div class="flex gap-12 w-10 mt-4 text-lg">
                  <i onclick="edit('${tweet_id}')" id="edit-post" class="editBtn fa-solid fa-pen cursor-pointer"></i>
                  <i onclick="deleteTweet('${tweet_id}')" class="fas fa-trash ml-auto cursor-pointer"></i>
                  <i class="fa-solid fa-message ml-auto"></i>
                  <i class="fa-solid fa-heart"></i>
                  <i class="fa-solid fa-retweet"></i>
                  <i class="fa-solid fa-share-nodes"></i>
              </div>
            </div>
          </div>
        </div>
      `
    document.querySelector("#tweet-post").insertAdjacentHTML("afterbegin", tweet_post)
  
    _one(".createTweet", form).value = ""
    document.querySelector("#tweetModal").classList.add("hidden")
  
    hideBrokenImage();
  }



            /////////// DELETE TWEET //////////////
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


//             /////////// UPDATE TWEET //////////////
// async function edit(tweet_id) {
//     const form = document.querySelector(".creatTweet")
//     // Get the button, set the data-await, and disable it

//     // user_id
//     const url = window.location.pathname;
//     const user_id = url.substring(url.lastIndexOf('/') + 1);
    
//     const connection = await fetch(`/tweets/${tweet_id}`, {
//         method : "PUT",
//         body: new FormData(form)
//     })

//     if( ! connection.ok ){
//         return
//     }
//     const res = await connection.json();
//     const tweet = res.tweet
//     const tweet_text = tweet.tweet_text
    
//     console.log(tweet_id);
//     toggleTweetModal()
//     console.log(tweet_text);
//     textEreaInput.value = tweet_text

// }















/////////// JQuery - hide borken image //////////////
function hideBrokenImage() {
    $('.userProfile').on("error", function() {
      $(this).attr('src', '/images/user_profile_pictures/default_profile_picture.png');
    });
  
    // Hide broken img when img not passed
    $(".tweetImg").on("error", function() {
      $(this).hide();
    });
}