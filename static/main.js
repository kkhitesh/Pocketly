function copy() {
  var txt = document.getElementById("copyLink");
  txt.select();
  txt.setSelectionRange(0, 99999);
  document.execCommand("copy");

  var tip = document.getElementById("tooltip");
  tip.innerHTML = "Copied: " + txt.value;
}

function out() {
  var tip = document.getElementById("tooltip");
  tip.innerHTML = "Copy to Clipboard";
}
