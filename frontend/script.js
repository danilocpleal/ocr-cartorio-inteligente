// Alternância entre abas
document.getElementById("uploadTab").onclick = () => {
  document.getElementById("uploadSection")?.classList.remove("hidden");
  document.getElementById("folderSection")?.classList.remove("hidden");
  document.getElementById("dirSection")?.classList.add("hidden");
};

document.getElementById("dirTab").onclick = () => {
  document.getElementById("uploadSection")?.classList.add("hidden");
  document.getElementById("folderSection")?.classList.add("hidden");
  document.getElementById("dirSection")?.classList.remove("hidden");
};

// Mostrar quantidade de arquivos selecionados
document.getElementById("folderInput")?.addEventListener("change", function () {
  const count = this.files.length;
  document.getElementById("folderCount").textContent =
    count > 0 ? `${count} arquivos selecionados` : "Nenhum arquivo selecionado";
});

// Upload de múltiplos arquivos (pasta)
document.getElementById("folderBtn")?.onclick = async () => {
  const files = document.getElementById("folderInput").files;
  if (files.length === 0) return alert("Selecione uma pasta com arquivos!");

  const formData = new FormData();
  for (const file of files) {
    formData.append("files", file); // 👈 nome do campo deve bater com o backend
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/upload-multiplos/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Erro ${response.status}: ${response.statusText}`);
    }

    const resultado = await response.json();
    document.getElementById("resultado").textContent = JSON.stringify(resultado, null, 2);
    alert(`${files.length} arquivos enviados com sucesso!`);
  } catch (error) {
    console.error("Erro ao enviar arquivos:", error);
    alert("Falha no envio. Verifique o backend e tente novamente.");
  }
};

// Processar diretório via caminho
document.getElementById("dirBtn")?.onclick = async () => {
  const caminho = document.getElementById("dirInput").value;
  if (!caminho) return alert("Informe o caminho do diretório!");

  try {
    const res = await fetch(`http://127.0.0.1:8000/processar/?caminho=${encodeURIComponent(caminho)}`);
    if (!res.ok) throw new Error(`Erro ${res.status}: ${res.statusText}`);

    const data = await res.json();
    document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    console.error("Erro ao processar diretório:", error);
    alert("Falha ao processar diretório.");
  }
};