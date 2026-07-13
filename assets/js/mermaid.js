function mermaidThemeVariables(isDark) {
  return {
    background: isDark ? "#1f1e1c" : "#f8f8f7",
    mainBkg: isDark ? "#282622" : "#fffaf2",
    secondBkg: isDark ? "#332f28" : "#f5ede1",
    primaryColor: isDark ? "#332f28" : "#fff4e2",
    secondaryColor: isDark ? "#273b37" : "#e9f4f1",
    tertiaryColor: isDark ? "#3c2b28" : "#fff1ed",
    primaryTextColor: isDark ? "#fffaf0" : "#1f1e1c",
    secondaryTextColor: isDark ? "#fffaf0" : "#1f1e1c",
    tertiaryTextColor: isDark ? "#fffaf0" : "#1f1e1c",
    primaryBorderColor: isDark ? "#b16f13" : "#b16f13",
    secondaryBorderColor: "#2f7f76",
    tertiaryBorderColor: "#c72e20",
    lineColor: isDark ? "#d6b171" : "#8a5b22",
    textColor: isDark ? "#fffaf0" : "#1f1e1c",
    nodeTextColor: isDark ? "#fffaf0" : "#1f1e1c",
    edgeLabelBackground: isDark ? "#282622" : "#fffaf2",
    clusterBkg: isDark ? "#282622" : "#fffaf2",
    clusterBorder: isDark ? "#6f5840" : "#d5b37c",
    noteBkgColor: isDark ? "#332f28" : "#fff4e2",
    noteTextColor: isDark ? "#fffaf0" : "#1f1e1c",
    noteBorderColor: "#b16f13",
    fontFamily:
      "PingFang SC,Hiragino Sans GB,Microsoft YaHei,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,segoe ui,Roboto,Arial,sans-serif",
    fontSize: "16px",
  };
}

function initMermaidLight() {
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    theme: "base",
    themeVariables: mermaidThemeVariables(false),
  });
}

function initMermaidDark() {
  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
    theme: "base",
    themeVariables: mermaidThemeVariables(true),
  });
}
