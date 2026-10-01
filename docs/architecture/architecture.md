# Smart Grocer — System Architecture

## Overview

Smart Grocer is a compact, AI-powered monitoring system designed to detect
fresh-produce spoilage, identify affected items, monitor inventory, and alert
shopkeepers.

## High-Level Architecture

```text
Camera ───────────────┐
                      │
VOC / Gas Sensors ────┤
                      │
Temperature/Humidity ─┤
                      │
Weight Sensor ────────┤
                      ▼
                Edge Processing
                      │
             ┌────────┴────────┐
             │                 │
        Computer Vision    Sensor Analysis
             │                 │
             └────────┬────────┘
                      ▼
                Sensor Fusion
                      │
                      ▼
              Spoilage Prediction
                      │
              ┌───────┴────────┐
              │                │
          Local Alert      Cloud Backend
                               │
                               ▼
                         Mobile Application
                               │
                               ▼
                          Shopkeeper
