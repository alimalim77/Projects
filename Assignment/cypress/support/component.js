// ***********************************************************
// This example support/component.js is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'

// Alternatively you can use CommonJS syntax:
// require('./commands')

import { mount } from 'cypress/react18'
import FormWithFocus from '../../app/src/App'

describe('FormWithFocus', () => {
    it('displays the submitted name', () => {
      cy.visit('http://localhost:3000');
      cy.get('input[type="text"]').type('John Doe');
      cy.get('input[type="submit"]').click();
      cy.get('p').should('have.text', 'Submitted name: John Doe');
    });
  });
Cypress.Commands.add('mount', mount)

// Example use:
// cy.mount(<MyComponent />)