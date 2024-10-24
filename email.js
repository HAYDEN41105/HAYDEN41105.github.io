var test = function(document)
{
    sender_name = document.getElementById("nameBox").value;
    email = document.getElementById("emailBox").value;
    comment = document.getElementById("submitBox").value;
    console.log("Email (not) sent!");
    console.log(sender_name, email, comment);
}

function SendEmail()
{
    email = document.getElementById('commentForm').children[1].value;
    if (!ValidateEmail(email)) {
        return;
    };
    emailjs.sendForm('service_gdhfpvl', 'template_tu4azsd', '#commentForm')
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
            window.open('contact_finish.html');
        }, function (error) {
            console.log('FAILED...', error);
            if (error.status == 412) {
                window.alert("One or more fields are invalid.")
                return;
            }
            window.alert("Form failed to send. Please try again later.")
        });
}

function ValidateEmail(input) {

    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if (input.match(validRegex)) {

        return true;

    } else {

        alert("Invalid email address!");

        return false;

    }

}