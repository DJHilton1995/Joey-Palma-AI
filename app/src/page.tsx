"use client";

import React from "react";

export default function Home() {
  return (
    <main className="min-h-screen bg-[#02030a] text-white flex items-center justify-center px-4 py-6">
      <div className="max-w-6xl w-full grid grid-cols-1 md:grid-cols-[1.2fr_1fr] gap-6">
        {/* LEFT: JOEY // NEON ARCADE */}
        <section className="relative rounded-2xl border border-[#ff003c55] bg-gradient-to-br from-[#050816] via-[#090020] to-[#00101f] p-6 shadow-[0_0_40px_#ff003c55] overflow-hidden">
          <div className="absolute inset-0 opacity-20 pointer-events-none">
            <div className="absolute -left-10 top-10 w-40 h-40 rounded-full bg-[#ff003c] blur-3xl" />
            <div className="absolute right-0 bottom-0 w-52 h-52 rounded-full bg-[#00eaff] blur-3xl" />
          </div>

          <div className="relative flex flex-col md:flex-row items-center gap-6">
            {/* Avatar block */}
            <div className="flex flex-col items-center gap-3">
              <div className="w-32 h-32 rounded-full border border-[#ff003c] bg-[#050816] flex items-center justify-center shadow-[0_0_30px_#ff003c]">
                <span className="text-xs tracking-[0.25em] text-[#ff8aa8]">
                  JOEY
                </span>
              </div>
              <div className="text-center">
                <p className="text-[0.7rem] tracking-[0.3em] text-[#ff8aa8] uppercase">
                  JOEY // NEON ARCADE
                </p>
                <p className="mt-1 text-xs text-[#9bdcff]">
                  Your personal AI helper center.
                </p>
              </div>
            </div>

            {/* Neon tablet / main CTA */}
            <div className="flex-1 space-y-4">
              <div className="rounded-xl border border-[#00eaff88] bg-[#020814] p-4 shadow-[0_0_30px_#00eaff55]">
                <p className="text-[0.7rem] tracking-[0.25em] text-[#9bdcff] uppercase mb-2">
                  MY AI HELPER CENTER
                </p>
                <p className="text-sm text-[#e2f6ff]">
                  Ask JoeyPalma to check your security, monitor your network, or
                  help with anything you’re working on.
                </p>

                <div className="mt-4 flex items-center gap-4">
                  {/* Fingerprint */}
                  <div className="w-16 h-16 rounded-full border border-[#00eaff] flex items-center justify-center bg-[#02101f] shadow-[0_0_25px_#00eaff]">
                    <div className="w-10 h-10 rounded-full border border-[#00eaff88] flex items-center justify-center">
                      <div className="w-6 h-6 rounded-full border border-[#00eaff55]" />
                    </div>
                  </div>

                  <button className="px-4 py-2 rounded-lg bg-[#ff003c] hover:bg-[#ff335c] text-xs font-semibold tracking-[0.2em] uppercase shadow-[0_0_25px_#ff003c]">
                    GET AI HELP
                  </button>
                </div>
              </div>

              {/* Ready / Settings */}
              <div className="flex gap-3">
                <button className="flex-1 px-3 py-2 rounded-lg border border-[#00eaff55] text-[0.7rem] tracking-[0.2em] uppercase text-[#9bdcff] bg-[#020814] hover:bg-[#041020]">
                  READY
                </button>
                <button className="flex-1 px-3 py-2 rounded-lg border border-[#ff003c55] text-[0.7rem] tracking-[0.2em] uppercase text-[#ff8aa8] bg-[#020814] hover:bg-[#120010]">
                  SETTINGS
                </button>
              </div>
            </div>
          </div>

          {/* Bottom: Chat input */}
          <div className="relative mt-6 rounded-xl border border-[#ffffff22] bg-[#050816] p-3 flex items-center gap-3">
            <input
              className="flex-1 bg-transparent outline-none text-xs placeholder:text-[#6b7a8f]"
              placeholder="Tell JoeyPalma what you need help with..."
            />
            <button className="px-3 py-1 rounded-md bg-[#00eaff] text-[0.7rem] font-semibold text-[#02030a] tracking-[0.15em] uppercase shadow-[0_0_20px_#00eaff]">
              SEND
            </button>
          </div>
        </section>

        {/* RIGHT: LOG + SECURITY AI */}
        <section className="space-y-4">
          {/* Past Help Log */}
          <div className="rounded-2xl border border-[#ffffff22] bg-[#050816] p-4 shadow-[0_0_25px_#00000088]">
            <p className="text-[0.7rem] tracking-[0.25em] text-[#9bdcff] uppercase mb-3">
              PAST HELP LOG
            </p>
            <ul className="space-y-2 text-xs text-[#c7d7ff]">
              <li>• What did you need help with?</li>
              <li>• Check on my security.</li>
              <li>• Is my network stable?</li>
              <li>• Block that bad file.</li>
              <li>• Update my security walls.</li>
            </ul>
          </div>

          {/* Security AI */}
          <div className="rounded-2xl border border-[#00ff8855] bg-[#02140c] p-4 shadow-[0_0_25px_#00ff8855]">
            <p className="text-[0.7rem] tracking-[0.25em] text-[#7dffb8] uppercase mb-2">
              MY SECURITY AI
            </p>
            <p className="text-xs text-[#c7ffd9] mb-3">
              EVERYTHING IS SAFE AND RUNNING WELL.
            </p>

            <p className="text-[0.65rem] tracking-[0.2em] text-[#7dffb8] uppercase mb-2">
              SYSTEM STATUS
            </p>
            <div className="flex gap-2">
              {["FIREWALL", "NETWORK", "FILES"].map((label) => (
                <div
                  key={label}
                  className="flex-1 rounded-lg bg-[#031a10] border border-[#00ff8855] px-2 py-2 flex flex-col gap-1"
                >
                  <span className="text-[0.6rem] text-[#7dffb8] tracking-[0.18em] uppercase">
                    {label}
                  </span>
                  <div className="flex items-center gap-1">
                    <span className="inline-block w-2 h-2 rounded-full bg-[#00ff88] shadow-[0_0_10px_#00ff88]" />
                    <span className="text-[0.6rem] text-[#c7ffd9]">
                      Stable
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
