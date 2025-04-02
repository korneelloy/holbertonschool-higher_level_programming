window.addEventListener('DOMContentLoaded', function() {
  getData().then((results) => {
    document.getElementById('hello').textContent = results.hello;
  });
});

async function getData() {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    return (json);
  } catch (error) {
    console.error(error.message);
  }
}
