function reverseString(str) {
    var charArray = str.split("");
    var reversedArray = charArray.reverse();
    var reversedStr = reversedArray.join("");
    return reversedStr;
  }
  
  // Test the function
  var input1 = "Hello, World!";
  var reversed1 = reverseString(input1);
  console.log("Reversed string 1:", reversed1);
  

  