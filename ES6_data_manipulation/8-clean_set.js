export default function cleanSet(set, startString) {
  if (!String.isString(startString) || startString === '') {
    return '';
  }  return Array.from(set)
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.legth))
    .join('-');
}
