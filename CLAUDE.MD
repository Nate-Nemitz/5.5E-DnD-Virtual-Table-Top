# CLAUDE.MD - AI Assistant Guide

## Project Overview

**5.5E DnD Virtual Table Top** is an open-source virtual tabletop (VTT) application for Dungeons & Dragons 5.5E. This project serves dual purposes:
1. A functional gaming platform for DMs and players
2. A learning project for full-stack software development

**Project Status**: Early development phase

## Tech Stack

### Backend
- **Language**: Python
- **Database**: SQLite (development) → PostgreSQL (production planned)
- **Real-time**: WebSockets (planned)

### Frontend
- **Languages**: HTML, CSS, JavaScript
- **Framework**: TBD

### Infrastructure
- Version Control: Git/GitHub
- License: Apache 2.0 + Creative Commons Attribution 4.0 (for D&D SRD 5.2.1 content)

## Current Features

- Dice rolling system (d4, d6, d8, d10, d12, d20, d100)
- SQL database integration for skill checks, feats, and inventory

## Development Priorities

### Immediate Roadmap
1. Character creation and management system
2. Combat tracking system
3. Spell casting mechanics
4. Real-time multiplayer support
5. Interactive character sheets

### Architecture Goals
- Clean, maintainable code
- Scalable database design
- Responsive frontend
- Professional-grade software practices

## Code Style & Conventions

### Python
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and single-purpose
- Prefer clarity over cleverness

### JavaScript
- Use modern ES6+ syntax
- Clear variable naming
- Comment complex logic
- Consistent indentation (prefer 2 or 4 spaces)

### Database
- Use meaningful table and column names
- Follow normalization principles
- Include proper indexes
- Document schema changes

### General Principles
- **KISS**: Keep It Simple, Stupid - avoid over-engineering
- **DRY**: Don't Repeat Yourself - but don't abstract too early
- **Security First**: Validate inputs, sanitize outputs, prevent SQL injection
- **Comments**: Explain *why*, not *what*
- **Testing**: Write tests for core functionality

## File Structure

```
5.5E-DnD-Virtual-Table-Top/
├── backend/          # Python backend code
├── frontend/         # HTML, CSS, JS files
├── database/         # SQL schemas and migrations
├── tests/            # Test files
├── docs/             # Additional documentation
├── README.md         # Project overview
├── CLAUDE.MD         # This file
└── LICENSE           # Apache 2.0 license
```

## Common Tasks & Guidance

### When Adding Features
1. Read existing code first to understand patterns
2. Check if similar functionality exists
3. Follow established naming conventions
4. Add appropriate error handling
5. Consider database schema impacts
6. Update documentation if needed

### When Fixing Bugs
1. Understand the root cause before fixing
2. Check for similar issues elsewhere
3. Add tests to prevent regression
4. Verify fix doesn't break other features

### When Refactoring
1. Only refactor what's necessary for the task
2. Maintain backward compatibility when possible
3. Don't add features during refactoring
4. Test thoroughly after changes

### Security Considerations
- Validate all user inputs
- Use parameterized queries (never string concatenation for SQL)
- Sanitize data displayed in HTML
- Implement proper authentication/authorization
- Handle errors gracefully without exposing internals
- Be mindful of OWASP Top 10 vulnerabilities

## D&D 5.5E Specific Notes

### Content Licensing
- Material from SRD 5.2.1 is used under CC BY 4.0
- Always attribute Wizards of the Coast for SRD content
- Proprietary D&D content (not in SRD) cannot be included

### Game Mechanics to Implement
- Character attributes (STR, DEX, CON, INT, WIS, CHA)
- Skill checks with modifiers
- Saving throws
- Combat rounds and initiative
- Spell slots and spell casting
- Character levels and experience
- Inventory management
- Character classes and races (from SRD)

## Testing Approach

- Write unit tests for core game logic
- Test database operations thoroughly
- Validate dice rolling statistics
- Test edge cases (critical hits, critical fails)
- Integration tests for full features
- Manual testing for UI/UX

## Documentation Standards

- Keep README.md updated with new features
- Document API endpoints when created
- Maintain database schema documentation
- Comment complex game rule implementations
- Reference SRD rules where applicable

## Git Workflow

- Feature branches for new functionality
- Descriptive commit messages
- Keep commits focused and atomic
- Test before committing
- Pull latest changes before starting work

## Questions & Support

- **Maintainer**: Nathaniel Dean Nemitz
- **LinkedIn**: https://www.linkedin.com/in/nate-nemitz/
- **Issues**: Submit via GitHub Issues

## Notes for Claude

- This is a learning project - explain your reasoning when helpful
- Balance professional practices with pragmatic solutions
- Suggest improvements but don't over-engineer
- Ask clarifying questions when requirements are unclear
- Reference specific D&D rules from SRD 5.2.1 when relevant
- Consider both beginner-friendly code and professional quality
- Be mindful that this project showcases professional development ability

## Project Philosophy

This VTT combines passion for D&D with professional software development. Code should be:
- **Functional**: It needs to work correctly
- **Readable**: Others should understand it
- **Maintainable**: Future changes should be easy
- **Professional**: Demonstrates real-world development skills
- **Learning-focused**: Showcases growth and best practices

---

*Last Updated: 2025-12-26*
