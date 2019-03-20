function NoImageSelect() {
  if (document.getElementById("id_picture").files.length === 0) {
    alert("Please Select An Image To Upload");
    return false;
  }
  if (
    !document
      .getElementById("id_picture")
      .files[0].name.match(/.(jpg|jpeg|png|gif)$/i)
  ) {
    alert("The file selected is not of an Image type");
    return false;
  }
  return true;
}

function showUploadOptions() {
    var display_button = document.getElementById("display-upload");
    var upload = document.getElementById("image-upload");
    var remove = document.getElementById("image-delete");
    display_button.style.display ="none";
    upload.style.display = "block";
    if (remove != null){
        remove.style.display = "none";
    }
}

function hideUploadOptions() {
    var display_button = document.getElementById("display-upload");
    var upload = document.getElementById("image-upload");
    var remove = document.getElementById("image-delete");
    display_button.style.display ="block";
    upload.style.display = "none";
    if (remove != null){
        remove.style.display = "block";
    }
    
}

$(document).ready(function(){
    //onclick of upload new image button or cancel button call appropirate function
    $("#displayB").click(function(){
        showUploadOptions();
    });
    $("#cancelB").click(function(){
        hideUploadOptions();
    });
    //When a new file is selected the labels text is replaced with the name of the file
    //inspired by https://tympanus.net/codrops/2015/09/15/styling-customizing-file-inputs-smart-way/
    $('input[type="file"]').change(function(e){
        var fileName;
        fileName = e.target.value.split( '\\' ).pop();
		if( fileName != null ){
			this.nextElementSibling.innerHTML = fileName;
        }
		else{
			this.nextElementSibling.innerHTML = "Select File";
        }
    });
});

