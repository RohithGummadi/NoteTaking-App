function deleteNote(noteId){
    fetch("/delete-note", {  //sending to delete-note end point
        method:"POST",
        body:JSON.stringify({noteId:noteId}),
        }).then((_res)=>{
            window.location.href="/";   //refresh the page
        });
}