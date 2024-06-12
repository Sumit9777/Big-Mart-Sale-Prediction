function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // Check if fields are filled
    if (username === '' || password === '') {
      alert('Please fill in all fields');
      return false;
    }

   
      var pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$";
    if (!pattern.test(email)) {
      alert('Please enter a valid email address');
      return false;
    }
  
  
    // Check if password is less than 8 characters
    if (password.length < 8) {
      alert('Password should be at least 8 characters long');
      return false;
    }
  
    // Additional authentication logic can be added here (e.g., checking against a database)
  
    // If all validations pass, the form will be submitted
    return true;
  }
  