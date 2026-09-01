# UI, UX, and accessibility

Review this dimension only when the change creates or alters a user-visible or assistive-technology-visible experience.

## Examine

- Conformance with the project's design system, tokens, components, spacing, typography, visual hierarchy, and interaction patterns.
- Responsive behavior, zoom, reflow, overflow, safe areas, orientation, and common desktop and mobile viewports.
- Loading, empty, error, success, disabled, offline, slow, partial, and destructive-action states.
- Clear affordances, feedback, confirmation, recovery, copy, validation, and preservation of user input.
- Keyboard reachability, logical tab order, visible focus, focus restoration, shortcuts, and escape behavior.
- Semantic elements, names, labels, roles, landmarks, headings, relationships, live announcements, and error association.
- Contrast, non-color cues, reduced motion, touch-target size, text resizing, and screen-reader behavior.
- Forms, dialogs, menus, tables, navigation, and dynamic content follow their expected interaction contracts.
- Perceived performance, layout stability, image behavior, and avoidance of blocking or disorienting transitions.
- Supplied screenshots or runtime evidence for materially affected states, when available.

## Evidence standard

Review source structure, semantics, state handling, styles, tests, and any supplied runtime evidence. Static inspection cannot prove visual or interaction correctness, so record unsupported runtime conclusions in `unknowns`. Do not run a comprehensive journey or create proof screenshots in this skill, and do not mark the source-review lane `owed` solely because screenshots were not supplied.
