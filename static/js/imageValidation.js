function NoImageSelect() {
  if (document.getElementById("id_picture").files.length == 0) {
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