while read p; do
  echo "$p" | tr '[:upper:]' '[:lower:]' >> words_lower
done <words

