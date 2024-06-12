function validateForm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
  
    // Check if fields are filled
    if (username === '' || email === '' || password === '') {
      alert('Please fill in all fields');
      return false;
    }
  
    // Check for a valid email format using a regular expression
    var pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$";
    if (!pattern.test(email)) {
      alert('Please enter a valid email address');
      return false;
    }
  
    // Additional authentication logic can be added here (e.g., checking against a database)
  
    // If all validations pass, the form will be submitted
    return true;
  }
  function redirectToLogin() {
    <a href="{{ url_for('login') }}"></a>
}
