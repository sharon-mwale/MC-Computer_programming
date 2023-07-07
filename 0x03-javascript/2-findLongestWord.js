function findLongestWord(sentence) {
    const words = sentence.split(' ');
    let longestWord = '';
  
    for (let i = 0; i < words.length; i++) {
      const currentWord = words[i];
      if (currentWord.length > longestWord.length) {
        longestWord = currentWord;
      }
    }
  
    return longestWord;
  }
  
  const sentence = "The quick brown fox jumped over the lazy dog";
  const longest = findLongestWord(sentence);
  console.log(`Longest word: ${longest}`);
  