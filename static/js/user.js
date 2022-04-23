
async function userUploadCoverImage(user_id) {
    const form = event.target.form

    const connection = await fetch(`/api-user-upload-cover/${user_id}`, {
        method: "POST",
        body: new FormData(form)
    })
    if (!connection.ok) {
        alert('Uuup... connection failed')
        return
    }
    const res = await connection.json()
    console.log(res.user_cover_image);
}