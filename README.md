# The Navigator

A production-grade RHEL system analysis tool demonstrating comprehensive Linux administration, security auditing, and automation capabilities.

## Overview

The Navigator is a progressive system reconnaissance tool built to audit Red Hat Enterprise Linux systems against operational and security best practices. The project showcases hands-on systems engineering through a "configure-then-verify" methodology, where manual system administration tasks are followed by automated validation tooling.

## Technical Implementation

**Architecture**: Single-binary design following the Filesystem Hierarchy Standard (FHS).

**Technology Stack**: Bash for system-level operations and command orchestration. Python for complex data parsing (JSON) and automation logic.

**Current Capabilities**:

*Configuration Phase*: Performed hands-on system administration tasks including creating a test user (`rhel_student`), establishing a secure configuration directory, implementing strict file permissions, managing system services (`httpd`), deploying containerized applications with Podman, and generating SSH key pairs with Ed25519 encryption.

*Validation Phase*: Built automated verification tooling that validates configuration through:

- **Core System**: OS fingerprinting, User account auditing, File permission validation.
- **Administration**: Service status monitoring (`systemctl`), Log analysis (`journalctl`), Storage/LVM usage checks.
- **Architecture**:
  - Network listener auditing (`ss`) to verify open ports.
  - Container runtime analysis using **Python** to parse Podman JSON output.
  - SSH key audit with permission validation (Ed25519 keys).
  - Automated backup generation with timestamped archives.

## Skills Demonstrated

- **RHEL System Administration**: User management, file permissions, service management (systemd), log aggregation (journalctl), storage monitoring (LVM), package management (dnf), SSH key management.
- **Containerization**: Managing OCI containers with Podman, inspecting container state via JSON.
- **Scripting & Automation**:
  - **Bash**: Argument parsing, error handling, text processing (awk/grep).
  - **Python**: Integration for JSON parsing and robust logic handling.
- **Security Practices**: Permission auditing, secure file handling, password database protection, SSH key security.
- **Version Control**: Atomic commits, feature-branch workflow.

## Usage Examples

```bash
# System information display
./bin/navigator --info

# Security and configuration validation
./bin/navigator --check

# User account enumeration
./bin/navigator --users

# Service, Log, and Storage checks (Module 2)
./bin/navigator --services
./bin/navigator --logs
./bin/navigator --disk

# Network, Container, and Backup tools (Module 3)
./bin/navigator --network
./bin/navigator --containers
./bin/navigator --ssh
./bin/navigator --backup
```

## Project Structure

```text
rhel-navigator/
├── bin/navigator        # Main executable (Bash)
├── etc/                 # Configuration files
├── lib/                 # Shared function libraries (Python/Bash)
├── var/logs/            # Runtime logs
├── var/cache/           # Temporary analysis data & Backups
└── share/docs/          # Generated reports
```

Built on Fedora 43 (RHEL upstream), demonstrating enterprise Linux administration patterns applicable across Red Hat ecosystems.
