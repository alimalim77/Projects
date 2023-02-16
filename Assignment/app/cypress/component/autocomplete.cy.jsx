import Autocomplete from "../component/autocomplete"
describe('Test the complete functionality', () => {
  it('Test react', () => {
      cy.mount(<Autocomplete/>)
      cy.get('input[type="text"]').type('John Doe');
      cy.get('input[type="submit"]').click();
      cy.wait(____);
      cy.get('p').should('have.text', 'Submitted name: John Doe');

  })
})

