
//Ensures that an image file has been selected before allowing the file-input form from being submitted.
function NoImageSelect() {
  if (document.getElementById("file-input").files.length == 0) {
    alert("Please Select An Image To Upload");
    return false;
  }
  if (
    !document
      .getElementById("file-input")
      .files[0].name.match(/.(jpg|jpeg|png|gif)$/i)
  ) {
    alert("The file selected is not of an Image type");
    return false;
  }
  return true;
}

//Shows the buttons and inputs for uploading a new profile picture and hides the button which calls it.
//Also hides the remove profile picture button if appropriate
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

//Hides the buttons and inputs for uploading a new profile picture.
//also reveals the button which can re-reveal the now hidden buttons and inputs for uploading a profile picture.
//reveals the remove profile picture btton if appropriate.
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

