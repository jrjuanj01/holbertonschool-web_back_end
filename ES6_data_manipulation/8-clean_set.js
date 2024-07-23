export default function cleanSet(set, startString) {
  return Array.from(set)
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.legth))
    .join('-');
}
