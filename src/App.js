import React, { useState } from "react";
import {
  Sun,
  Moon,
  Music,
  ThermometerSun,
  Activity,
  Brain,
  Eye,
  Mic,
  Settings,
  Check,
  Volume2,
  Wind,
  Heart,
  PlayCircle,
  PauseCircle,
  Leaf,
} from "lucide-react";

const IntegratedDashboard = () => {
  const [activeTab, setActiveTab] = useState("dashboard");
  const [temperature, setTemperature] = useState(72);
  const [lightIntensity, setLightIntensity] = useState(80);
  const [volume, setVolume] = useState(60);
  const [isRelaxationActive, setIsRelaxationActive] = useState(false);
  const [selectedAmbience, setSelectedAmbience] = useState("nature");

  const renderWelcomeSection = () => (
    <div className="bg-gradient-to-br from-blue-50 to-purple-50 p-6 rounded-lg shadow-md mb-6">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-blue-900">Welcome to ZenSense AI</h2>
          <p className="text-gray-600">Your Intelligent Driving Companion</p>
        </div>
        <div className="bg-green-100 px-4 py-2 rounded-full flex items-center">
          <Activity className="w-5 h-5 text-green-600 mr-2" />
          <span className="text-green-700">System Active</span>
        </div>
      </div>
    </div>
  );

  const renderAnalytics = () => (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      {[{
        title: "Facial Analysis",
        icon: Eye,
        stats: [{ label: "Attention", value: "98%" }, { label: "Fatigue", value: "Low" }]
      }, {
        title: "Voice Analysis",
        icon: Mic,
        stats: [{ label: "Stress Level", value: "Low" }, { label: "Tone", value: "Calm" }]
      }, {
        title: "Overall State",
        icon: Brain,
        stats: [{ label: "Mood", value: "Positive" }, { label: "Focus", value: "High" }]
      }].map(({ title, icon: Icon, stats }, idx) => (
        <div key={idx} className="bg-white p-4 rounded-lg shadow-md">
          <div className="flex items-center mb-3">
            <Icon className="w-5 h-5 text-indigo-500 mr-2" />
            <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
          </div>
          <div className="space-y-2">
            {stats.map(({ label, value }, i) => (
              <div key={i} className="flex justify-between">
                <span className="text-gray-600">{label}</span>
                <span className="text-indigo-600">{value}</span>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );

  const renderControls = () => (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
      {[{
        label: "Temperature",
        value: `${temperature}°F`,
        icon: ThermometerSun,
        min: 60,
        max: 85,
        state: temperature,
        setState: setTemperature
      }, {
        label: "Lighting",
        value: `${lightIntensity}%`,
        icon: Sun,
        min: 0,
        max: 100,
        state: lightIntensity,
        setState: setLightIntensity
      }, {
        label: "Audio",
        value: `${volume}%`,
        icon: Volume2,
        min: 0,
        max: 100,
        state: volume,
        setState: setVolume
      }].map(({ label, value, icon: Icon, min, max, state, setState }, idx) => (
        <div key={idx} className="p-4 bg-white rounded-lg shadow-md">
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center space-x-2">
              <Icon className="w-5 h-5 text-blue-500" />
              <span>{label}</span>
            </div>
            <span>{value}</span>
          </div>
          <input
            type="range"
            min={min}
            max={max}
            value={state}
            onChange={(e) => setState(Number(e.target.value))}
            className="w-full"
          />
        </div>
      ))}
    </div>
  );

  const renderRelaxationControls = () => (
    <div className="bg-white p-6 rounded-lg shadow-md mb-6">
      <div className="flex items-center mb-4">
        <Leaf className="w-6 h-6 text-green-500 mr-2" />
        <h3 className="text-xl font-semibold text-gray-800">Relaxation Zone</h3>
      </div>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            {isRelaxationActive ? (
              <PauseCircle
                className="w-12 h-12 text-green-500 cursor-pointer"
                onClick={() => setIsRelaxationActive(false)}
              />
            ) : (
              <PlayCircle
                className="w-12 h-12 text-green-500 cursor-pointer"
                onClick={() => setIsRelaxationActive(true)}
              />
            )}
            <div>
              <p className="font-medium text-gray-800">Ambient Sound</p>
              <p className="text-gray-500 text-sm">
                {isRelaxationActive ? "Playing" : "Paused"}
              </p>
            </div>
          </div>
          <div className="flex space-x-2">
            {["nature", "rain", "waves", "white noise"].map((ambience) => (
              <button
                key={ambience}
                className={`px-4 py-2 rounded-lg text-sm ${
                  selectedAmbience === ambience ? "bg-green-500 text-white" : "bg-gray-200"
                }`}
                onClick={() => setSelectedAmbience(ambience)}
              >
                {ambience}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="w-full max-w-6xl mx-auto p-6 space-y-6">
      {renderWelcomeSection()}

      <div className="flex space-x-4 mb-6">
        <button
          className={`px-4 py-2 rounded-lg text-sm ${
            activeTab === "dashboard" ? "bg-blue-500 text-white" : "bg-gray-200"
          }`}
          onClick={() => setActiveTab("dashboard")}
        >
          Dashboard
        </button>
        <button
          className={`px-4 py-2 rounded-lg text-sm ${
            activeTab === "controls" ? "bg-blue-500 text-white" : "bg-gray-200"
          }`}
          onClick={() => setActiveTab("controls")}
        >
          Controls
        </button>
      </div>

      {activeTab === "dashboard" ? (
        <>
          {renderAnalytics()}
          {renderRelaxationControls()}
        </>
      ) : (
        renderControls()
      )}
    </div>
  );
};

export default IntegratedDashboard;
