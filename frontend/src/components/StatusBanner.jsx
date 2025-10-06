/**
 * Mensagem de status para feedback visual rápido.
 */
function StatusBanner({ type = 'info', message }) {
  if (!message) return null

  const variants = {
    info: 'bg-blue-50 text-blue-700 border-blue-200',
    error: 'bg-rose-50 text-rose-700 border-rose-200',
    success: 'bg-emerald-50 text-emerald-700 border-emerald-200',
  }

  return (
    <div className={`rounded-2xl border px-4 py-3 text-sm ${variants[type]}`}>
      {message}
    </div>
  )
}

export default StatusBanner
