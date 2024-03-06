function view_action(key) {
    var x = document.getElementById(key);
    if (x.style.display === "none") {
        console.log("display as block")
        x.style.display = "block";
    } else {
        console.log("display as NONE")
        x.style.display = "none";
    }
}
/*adj 1 */




function add_msg(msg_item) {
    var msg_model_1 = document.getElementById("view_msg");
    var msg_model_2 = document.querySelectorAll(".msg_2");
    var msg_sec = document.getElementById("msg_item")
    console.log("You added msg :", msg_sec.value);
    if (msg_model_1.innerHTML) {
        msg_model_1.innerHTML += '<div class="msg_1">' + msg_sec.value + '</div>';
        console.log("You added msg :", msg_sec.value);
    } else {

        msg_model_1.innerHTML = '<div class="msg_1">' + msg_sec.value + '</div>';
        console.log("You added msg :", msg_sec.value);
    }

    msg_sec.value = "";

}