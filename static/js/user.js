
async function userUploadCoverImage(user_id) {
    const form = event.target.form

    const connection = await fetch(`/api-user-upload-cover/${user_id}`, {
        method: "PUT",
        body: new FormData(form)
    })
    if (!connection.ok) {
        alert('Uuup... connection failed')
        return
    }
    try {
        const res = await connection.json();
        console.log(res.image_cover_image);


        let banner = document.querySelector(".banner");
        let user_cover_image = `
            <img class="cover object-cover w-full" src="/static/images/user_cover_image/${res.image_cover_image}" onError="this.onerror=null;this.src='/static/images/user_profile_pictures/default_profile_picture.png';">
        `
        document.querySelector(".cover-to-remove").remove()
        banner.insertAdjacentHTML("afterbegin", user_cover_image)
        document.querySelector(".spa-modal-cover-image").style.display = "none"
        

    } catch (error) {
        console.log("Error: ", error.message);
    }
    
}