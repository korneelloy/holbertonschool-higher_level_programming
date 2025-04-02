async function getData() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    return (json.results);
  } catch (error) {
    console.error(error.message);
  }
}

getData().then((results) => {
  const list = document.getElementById('list_movies');
  for (const result of results) {
    const item = document.createElement ('li');
    var itemText = document.createTextNode(result.title);
		item.appendChild(itemText);
    list.appendChild(item);
  }
});
