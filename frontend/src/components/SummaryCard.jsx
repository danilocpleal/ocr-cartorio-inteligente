/**
 * Componente reutilizável para exibir estatísticas do processamento.
 */
function SummaryCard({ title, value, description, icon: Icon, tone = 'blue' }) {
  const tones = {
    blue: 'bg-blue-50 text-blue-600 border-blue-100',
    emerald: 'bg-emerald-50 text-emerald-600 border-emerald-100',
    slate: 'bg-slate-50 text-slate-600 border-slate-100',
  }

  return (
    <div className={`rounded-2xl border p-6 shadow-sm transition hover:-translate-y-0.5 hover:shadow-lg ${tones[tone]}`}>
      <div className="flex items-center gap-3">
        {Icon ? (
          <span className="flex h-10 w-10 items-center justify-center rounded-full bg-white text-current">
            <Icon className="h-5 w-5" />
          </span>
        ) : null}
        <div>
          <p className="text-xs uppercase tracking-wide text-slate-400">{title}</p>
          <p className="mt-1 text-2xl font-semibold text-slate-800">{value}</p>
          {description ? <p className="mt-2 text-sm text-slate-500">{description}</p> : null}
        </div>
      </div>
    </div>
  )
}

export default SummaryCard
