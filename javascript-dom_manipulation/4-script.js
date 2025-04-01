document.getElementById('add_item').addEventListener('click', function(){
  const newItem = document.createElement ('li');
  const newItemText = document.createTextNode("Item");
  newItem.appendChild(newItemText);
  document.querySelector('ul.my_list').appendChild(newItem);
}
)
