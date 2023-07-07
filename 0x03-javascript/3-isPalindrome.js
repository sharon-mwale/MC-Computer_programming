function isPalindrome(str) {
    // Remove non-alphanumeric characters from the string and convert to lowercase
    const alphanumericStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  
    // Reverse the string
    const reversedStr = alphanumericStr.split('').reverse().join('');
  
    // Check if the reversed string is equal to the original string
    return alphanumericStr === reversedStr;
  }
  
  console.log(isPalindrome("racecar")); // Output: true
  console.log(isPalindrome("hello"));   // Output: false
  
  