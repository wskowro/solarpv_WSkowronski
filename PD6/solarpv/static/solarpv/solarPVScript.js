

function checkUsername()
{
	if (this.value.length > 8)
	{
		document.getElementById('usernameCheck').innerHTML = "Username cannot be over 8 characters";
	}
	else
	{
		document.getElementById('usernameCheck').innerHTML = "";
	}
}

function checkPassword()
{
	if (this.value.length > 8)
	{
		document.getElementById('passwordCheck').innerHTML = "Password cannot be over 8 characters";
	}
	else if (this.value.search(/[a-z]/) < 0)
	{
		document.getElementById('passwordCheck').innerHTML = "Password needs atleast 1 lowercase letter";
	}
	else if (this.value.search(/[A-Z]/) < 0)
	{
		document.getElementById('passwordCheck').innerHTML = "Password needs atleast 1 uppercase letter";
	}
	else if (this.value.search(/[0-9]/) < 0)
	{
		document.getElementById('passwordCheck').innerHTML = "Password needs atleast 1 number";
	}
	else
	{
		document.getElementById('passwordCheck').innerHTML = "";
	}
}

document.getElementById("user").addEventListener('blur', checkUsername);
document.getElementById("pass").addEventListener('blur', checkPassword);


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    document.getElementById("myLoc").innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  document.getElementById("myLoc").innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
