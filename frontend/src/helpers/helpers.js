export const camelToText = (text) => {
  return text.replace(/[\w]([A-Z])/g, function (m) {
    return m[0] + " " + m[1];
  }).toLowerCase();
};

