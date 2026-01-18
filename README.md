# The Navigator

A production-grade RHEL system analysis tool demonstrating comprehensive Linux administration, security auditing, and automation capabilities.

## Overview

The Navigator is a progressive system reconnaissance tool built to audit Red Hat Enterprise Linux systems against operational and security best practices. The project showcases hands-on systems engineering through a "configure-then-verify" methodology, where manual system administration tasks are followed by automated validation tooling.

## Technical Implementation

**Architecture**: Single-binary design following the Filesystem Hierarchy Standard (FHS).

**Technology Stack**: Bash for system-level operations and command orchestration.

**Current Capabilities**:

*Configuration Phase*: Performed hands-on system administration tasks including creating a test user (`rhel_student`) with specific UID assignment (2000), establishing a secure configuration directory (`/opt/navigator-secrets`), and implementing strict file permissions (600) for sensitive data storage. These tasks demonstrate practical knowledge of user management (`useradd`), filesystem hierarchy usage, and security-conscious permission assignment.

*Validation Phase*: Built automated verification tooling that validates the manual configuration through:

- System reconnaissance and OS fingerprinting via `/etc/os-release` parsing
- User account auditing with `getent` and UID-based filtering for regular user identification
- File permission validation using `stat` with normalized octal comparison
- Security compliance checks for critical system files (`/etc/shadow` with 000/400 permission validation)
- Color-coded terminal output for operational clarity

## Skills Demonstrated

- **RHEL System Administration**: User management with UID control, file permissions, filesystem hierarchy, system file analysis
- **Shell Scripting**: Command-line argument parsing with case statements, error handling with `set -euo pipefail`, modular function design
- **Security Practices**: Permission auditing, secure file handling, password database protection
- **Version Control**: Atomic commits with descriptive messages, feature-branch workflow
- **Code Quality**: Defensive programming with input validation and graceful degradation

## Usage Examples

```bash
# System information display
./bin/navigator --info

# Security and configuration validation
./bin/navigator --check

# User account enumeration
./bin/navigator --users
```

## Project Structure

```
rhel-navigator/
├── bin/navigator        # Main executable (Bash)
├── etc/                 # Configuration files
├── lib/                 # Shared function libraries
├── var/logs/            # Runtime logs
├── var/cache/           # Temporary analysis data
└── share/docs/          # Generated reports
```

Built on Fedora 43 (RHEL upstream), demonstrating enterprise Linux administration patterns applicable across Red Hat ecosystems.
