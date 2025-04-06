document.getElementById('submitBtn').addEventListener('click', async () => {
  const id = document.getElementById('userId').value.trim();
  const password = document.getElementById('password').value.trim();
  const action = document.getElementById('actionType').value;
  const url = "www.example.com";

  if (!id || !password || !action) {
    alert('Please fill all fields');
    return;
  }

  const data = { url, id, password, action };

  try {
    const response = await fetch('https://fastapi-backend-usyf.onrender.com/run-task', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    alert(result.message || 'Request sent!');
  } catch (err) {
    console.error(err);
    alert('Error sending request');
  }
});
