// const userTweetPost = document.querySelector('#user-tweet-post')
// console.log(userTweetPost)
// const renderUserTweets = (post, tweet_id) => {
//     output += `
//     <div id="${tweet_id}" class="p-4 border-t border-slate-200">
//     <div class="flex">
//       <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/user_profile_pictures/${post.user_profile_picture}">
//       <div class="w-full pl-4">
//         <!-- first name - username/ text -->
//           <div id="user-info" class="flex">
//           <p class="font-bold pr-2">
//                 <a href="/user-tweets/${post.user_id}" onclick="spa(); return false">
//                 ${post.user_first_name} ${post.user_last_name}
//                 </a>
//               </p>
//             <p class="font-thin">
//               ${post.user_name}
//             </p>                        
//           </div>
//         <div id="tweet-text" class="pt-2">
//           ${post.tweet_text}
//         </div>
        
//         <div id="tweet-image">
//           <img class="mt-2 w-full object-cover h-80 tweetImg" src="/images/user_content_images/${post.tweet_image}">
//         </div>
//         <div class="flex gap-12 w-10 mt-4 text-lg">
//             <i id="delete-post" onclick="edit('${tweet_id}')" class="editBtn fa-solid fa-pen cursor-pointer"></i>
//             <i onclick="deleteTweet('${tweet_id}')" class="fas fa-trash ml-auto cursor-pointer"></i>
//             <i class="fa-solid fa-message ml-auto"></i>
//             <i class="fa-solid fa-heart"></i>
//             <i class="fa-solid fa-retweet"></i>
//             <i class="fa-solid fa-share-nodes"></i>
//         </div>
//       </div>
//     </div>
//   </div>
//   `;
//   userTweetPost.innerHTML = output;
//   hideBrokenImage();
  
//   }



// ////  test /////
// fetch('/user-tweets')
//     .then(res => res.json())
//     .then(data => {
//         data.tabs.forEach(post => {
//             // console.log(post) 
//             // console.log(data.tweet_id)
//             // const tweet_id = data.tweet_id
//             // renderUserTweets(post, tweet_id)
//             console.log(post)
//         })
       
// })
// ///////////////