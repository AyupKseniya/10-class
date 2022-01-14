function show (details)
{
	var elem = document.getElementById (details);
	if (elem)
		elem.style.display="block";
}

function check()
{
if (otvet.answer.value == "Сортавала")
	alert("Правильно!");
else alert("Неправильно!");
}