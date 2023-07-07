function calculateAverageGrade(grades){
  var sum = 0;

  for (let i = 0; i < grades.length; i++){
      sum += grades[i];
  }
  return sum/ grades.length
}
console.log("The average is: ", calculateAverageGrade([85, 90, 78, 92, 88]))

  
