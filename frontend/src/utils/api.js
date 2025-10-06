const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

/**
 * Chama o endpoint de processamento com os arquivos selecionados.
 */
export async function processarDocumentos(files) {
  const formData = new FormData()
  files.forEach((file) => formData.append('files', file))

  const response = await fetch(`${API_BASE_URL}/upload/multiplos`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    const errorMessage = await response.text()
    throw new Error(errorMessage || 'Falha ao processar documentos')
  }

  return response.json()
}

export function formatarData(isoString) {
  if (!isoString) return ''
  try {
    const data = new Date(isoString)
    return new Intl.DateTimeFormat('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    }).format(data)
  } catch (error) {
    return isoString
  }
}
